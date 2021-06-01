import module
import pytest
import numpy as np


type_error_msg_1 = 'Please input int, float, list or ndarray'

def convert_to_array(obj):
    if isinstance(obj, list):
        obj = np.array(obj)
    elif isinstance(obj, (int, float)):
        obj = np.array([obj])
    return obj


class TestFactorial:
    @pytest.mark.parametrize('n, compare',
                             [(0, 1),
                              (1, 1),
                              (2, 2),
                              (3, 6),
                              (4, 24),
                              (4.99, 24),
                              ])
    def test_factorial_positive(self, n, compare):
        assert module.factorial(n) == compare

    def test_factorial_negative_or_empty(self):
        message = 'Factorial cannot be negative or empty'
        assert module.factorial(-1) == message
        assert module.factorial() == message

    @pytest.mark.parametrize('a', [
        'ы', '1', [], (), {}, {1}, None, ''])
    def test_factorial_non_integer(self, a):
        assert module.factorial(a) == 'Factorial must be integer'


class TestCos:
    @pytest.mark.parametrize('x, compare', [
        (0, 1),
        (0.5, 0.8775825618903728),
        (1, 0.5403023058681397),
        (2, -0.41614683654756973),
        (98, -0.8192882453386182),
        (-1.2, 0.3623577544766735),
        (-21.345987, -0.799002617833374),
        (-24397, 0.8204790837943198),

        ([0, 0.5], [1, 0.8775825618903728]),

        ([-2.45, -0, 18.067831, 0.7096993791863329],
         [-0.7702312540719439, 1.0, 0.7096993791863329,
          0.7585577965185062]),
    ])
    def test_cos(self, x, compare):
        assert module.cos(x, False).tolist() == (
            convert_to_array(compare)).tolist()

    @pytest.mark.parametrize('x', [
        'ы', '1', (), {}, {1}, None, ''])
    def test_cos_wrong_data_types(self, x):
        assert module.cos(x, False) == type_error_msg_1


class TestSin:
    @pytest.mark.parametrize('x, compare', [
        (0, 0),
        (0.5, 0.479425538604203),
        (1, 0.8414709848078965),
        (2, 0.909297426825641),
        (98, -0.573381871984738),
        (-1.2, -0.9320390859672263),
        (-21.345987, -0.6013275453091816),
        (-24397, 0.5716765458334229),

        ([0, 0.5], [0, 0.479425538604203]),

        ([-2.45, -0, 18.067831, 0.7096993791863329],
         [-0.6377647021316261, 0.0, -0.7045046424137558,
          0.6516057622067106]),
    ])
    def test_sin(self, x, compare):
        assert module.sin(x, False).tolist() == (
            convert_to_array(compare)).tolist()

    @pytest.mark.parametrize('x', [
        'ы', '1', (), {}, {1}, None, ''])
    def test_sin_wrong_data_types(self, x):
        assert module.sin(x, False) == type_error_msg_1


class TestTan:
    @pytest.mark.parametrize('x, compare', [
        (0, 0),
        (0.5, 0.54630249),
        (1, 1.557407725),
        (3, -0.142546543),
        (98, 0.699853654),
        (-1.2, -2.572151622),
        (-21.345987, 0.752597716),
        (-24397, 0.696759439),

        ([0, 0.5], [0, 0.54630249]),

        ([-2.45, -0, 18.067831, 0.7096993791863329],
         [0.828017169, 0.0, 0.859006084, -0.99268037]),
    ])
    def test_tan(self, x, compare):
        assert module.tan(x, graph=False).tolist() == (
            convert_to_array(compare)).tolist()

    @pytest.mark.parametrize('x', ['ы', '1', (), {}, {1}, None, ''])
    def test_tan_wrong_data_types(self, x):
        assert module.tan(x, False) == type_error_msg_1


class TestCotan:
    @pytest.mark.parametrize('x, compare', [

        (0.5, 1.830487722),
        (1, 0.642092616),
        (98, 1.428870157),
        (-1.2, -0.388779569),
        (-21.345987, 1.328731112),
        (-24397, 1.435215577),

        ([-2.45, 18.067831],
         [1.207704427, -1.007373602]),
    ])
    def test_cotan(self, x, compare):
        assert module.cotan(x, graph=False).tolist() == (
            convert_to_array(compare)).tolist()

    def test_cotan_zero(self):
        assert module.cotan(0, graph=False) == (
            'x cannot be 0')

    @pytest.mark.parametrize('x', ['ы', '1', (), {}, {1}, None, ''])
    def test_cotan_wrong_data_types(self, x):
        assert module.cotan(x, False) == type_error_msg_1


class TestLinear:
    @pytest.mark.parametrize('k, x, compare', [
        (10, [1, -19, 4], [-190, 10, 40]),
        (-3, [-19], [57]),
        (10, [-19.2], [-192]),
        (10, -19, [-190]),
        (10, -19.2, [-192]),
        (2.8, -19, [-53.2]),
        (2.8, [1, -19, 4], [-53.2, 2.8, 11.2]),
    ])
    def test_linear_no_b(self, k, x,compare):
        result = module.linear(k, x, graph=False).tolist()
        result = [round(value, 14) for value in result]
        compare = convert_to_array(compare).tolist()
        assert np.array_equal(result, compare), (
                f'{result} != {compare}')

    @pytest.mark.parametrize('k, x, b, compare', [
        (10, [1, -19, 4], 1, [-189, 11, 41]),
        (10, [1, -19, 4], 126, [-64, 136, 166]),
        (-2, [1, -19, 4], -18, [20, -20, -26]),
    ])
    def test_linear_with_b(self, k, x, b, compare):
        result = module.linear(k, x, b, graph=False).tolist()
        result = [round(value, 14) for value in result]
        compare = convert_to_array(compare).tolist()
        assert np.array_equal(result, compare), (
                f'{result} != {compare}')

    @pytest.mark.parametrize('k, x, b, compare', [
        (10, [1, -19, 4], 1, [-189, 11, 41]),
        (10, [1, -19, 4], 126, [-64, 136, 166]),
        (-2, [1, -19, 4], -18, [20, -20, -26]),
        (-2.8, [1, -19, 4], 13, [66.2, 10.2, 1.8]),
    ])
    def test_linear_with_ndarray(self, k, x, b, compare):
        x = np.array(x)
        result = module.linear(k, x, b, graph=False).tolist()
        result = [round(value, 13) for value in result]
        compare = convert_to_array(compare).tolist()
        assert np.array_equal(result, compare), (
                f'{result} != {compare}')

    @pytest.mark.parametrize('k, x, b', [
        ('10', [1, -19, 4], 1),
        (10, 'a', 126),
        (10, 19, '1'),
    ])
    def test_linear_wrong_types(self, k, x, b):
        assert module.linear(
            k, x, b, graph=False) == type_error_msg_1


class TestPower:
    @pytest.mark.parametrize('x, n, compare', [
        ([3, 2], 4, [16, 81]),
        (-6, 0, [1]),

        ([-24.12, 0, 38.444], 4,
          [338461.45249536, 0, 2184310.00148097]),

        (3, 4, [81]),
        (-2.5, 3, [-15.625]),
        (1/2, 4, [0.0625]),
        (-1/4, 4, [0.00390625]),
    ])
    def test_power_x_n(self,x, n, compare):
        result = module.power(x, n, graph=False)
        result = [round(value, 8) for value in result]
        assert np.array_equal(result, compare), (
                f'{result} != {compare}')

    @pytest.mark.parametrize('x, n, a, b, c, compare', [
        ([3, 2], 4, 1, 0, 0, [16, 81]),
        (3, 2, 1, 0, 0, [9]),

        ([-24.12, 0, 38.444], 2, 5, 7, -25,
        [2715.032, -25, 7633.81368]),
        #
        (3.9, -2, 1, 0, 0, [0.06574622]),
        (3.9, -1, 1, 0, 0, [0.25641026]),
        (3.9, -1, 12, 4, 25, [0.25641026]),
        (-3.9, -1, 12, 4, -25, [-0.25641026]),
        (4, 2.6, 5.4, -7.4, -125.2, [36.75834736]),
    ])
    def test_power_x_n_a_b_c(self, x, n, a, b, c, compare):
        result = module.power(x, n, a, b, c, graph=False)
        result = [round(value, 8) for value in result]
        assert np.array_equal(result, compare), (
            f'{result} != {compare}')


class TestExponential:
    @pytest.mark.parametrize('x, a, compare', [
        (3, 4, [64]),
        ([7, 12], 4, [16384, 16777216]),
        ([-7, 12], 4, [6.103515625e-05, 16777216]),
        ([-7, 12], 4, [6.103515625e-05, 1.6777216e+07]),
        (-5, 2, [0.03125]),
        (1/2, 2, [1.4142135381698608]),
        (-1/4, 4, [0.7071067690849304]),
        (-0.75, 5, [0.29906976222991943]),
    ])
    def test_exponential(self, x, a, compare):
        result = module.exponential(x, a, graph=False).tolist()
        compare = convert_to_array(compare).tolist()
        assert result == compare, f'{result} != {compare}'

    @pytest.mark.parametrize('x, a', [
        (3, 1),
        (3, 0),
        (3, -1),
    ])
    def test_exponential_wrong_a(self, x, a):
        result = module.exponential(x, a, graph=False)
        message = 'a should be !=1 and >0'
        assert result == message, f'{result} != {message}'

    @pytest.mark.parametrize('x, a', [
        ('ы', 2),
        ('1', 2) ,
        ((), 2),
        ({}, 2),
        ({1}, 2),
        (None, 2),
        ('', 2),
        (2, 'ы'),
        (2, '1'),
        (2, ()),
        (2, {}),
        (2, {1}),
        (2, None),
        (2, ''),
    ])
    def test_exponential_wrong_data_types(self, x, a):
        assert module.exponential(
            x, a, False) == type_error_msg_1


class TestLn:
    @pytest.mark.parametrize('x, compare', [
        (4, [1.3862943765301174]),
        ([4, 5], [1.3862943765301174, 1.6094379223824082]),
        (1.3, [0.2623642610242536]),
    ])
    def test_ln(self, x, compare):
        result = module.ln(x, graph=False).tolist()
        compare = convert_to_array(compare).tolist()
        assert result == compare, f'{result} != {compare}'

    @pytest.mark.parametrize('x', [-1, 0])
    def test_ln_negative_and_zero(self, x):
        assert module.ln(x, graph=False) == 'x should be > 0'


class TestLog:
    @pytest.mark.parametrize('x, base', [
        ('ы', 2),
        ('1', 2),
        ((), 2),
        ({}, 2),
        ({1}, 2),
        (None, 2),
        ('', 2),
        (2, 'ы'),
        (2, '1'),
        (2, ()),
        (2, {}),
        (2, {1}),
        (2, None),
        (2, ''),
    ])
    def test_log_wrong_data_types(self, x, base):
        assert module.log(x, base, False) == type_error_msg_1



class TestAtan:
    @pytest.mark.parametrize('x, compare', [
        (0, 0.0),
        (0.5, 0.4636476090008178),
        (1, 0.7853981682575836),
        (2, 1.1071487177940789),
        (98, 1.5605925993009424),
        (-1.2, -0.8760581327800069),

        ([0, 0.5], [0.0, 0.4636476090008178])])
    def test_atan(self, x, compare):
        assert module.arctan(x, False).tolist() == (
            convert_to_array(compare)).tolist()

    @pytest.mark.parametrize('x', [
        'ы', '1', (), {}, {1}, None, ''])
    def test_cos_wrong_data_types(self, x):
        assert module.arctan(x, False) == type_error_msg_1


class TestAcot:
    @pytest.mark.parametrize('x, compare', [
        (0.5, 1.1071972726983763),
        (1, 0.7853981682575836),
        (2, 0.4636476090008178),
        (98, 0.010203727493954233),
        (-1.2, 2.4468543771735134),

        ([1, 2], [0.7853981682575836, 0.4636476090008178])])
    def test_acot(self, x, compare):
        assert module.arccot(x, False).tolist() == (
            convert_to_array(compare)).tolist()

    @pytest.mark.parametrize('x', [
        'ы', '1', (), {}, {1}, None, ''])
    def test_cos_wrong_data_types(self, x):
        assert module.arccot(x, False) == type_error_msg_1


class TestAsin:
    @pytest.mark.parametrize('x, compare', [
        (0.5, 0.5235987755985149),
        (1, 1.5708),
        (0, 0.),
        (0.1, 0.1001674211615598),
        (-0.7, -0.7753975001150127),

        ([0.5, 1], [0.5235987755985149, 1.5708])])
    def test_asin(self, x, compare):
        assert module.arcsin(x, False).tolist() == (
            convert_to_array(compare)).tolist()

    @pytest.mark.parametrize('x', [
        'ы', '1', (), {}, {1}, None, ''])
    def test_cos_wrong_data_types(self, x):
        assert module.arcsin(x, False) == type_error_msg_1


class TestAcos:
    @pytest.mark.parametrize('x, compare', [
        (0.5, 1.0472076798457144),
        (-1, 3.141592653589793),
        (0.1, 1.8168787999221883),
        (0.2, 1.3992455869081994),
        (-0.7, 2.3461938166869043),
        ([0.5, 1], [1.0472076798457144, 0.])])
    def test_acos(self, x, compare):
        assert module.arccos(x, False).tolist() == (
            convert_to_array(compare)).tolist()

    @pytest.mark.parametrize('x', [
        'ы', '1', (), {}, {1}, None, ''])
    def test_cos_wrong_data_types(self, x):
        assert module.arccos(x, False) == type_error_msg_1