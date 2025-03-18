import random

"""
num:
**kwargs:
"""
def random_fun(num, **kwargs):
    result = list()
    for _ in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['data_range'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['data_range'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['data_range']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(tmp)
    return result




if __name__ == '__main__':
    # test_case = [{
    #     "num":5,
    #     "kwargs"
    # }]
    print(random_fun(5, **{
        "int": {
            "data_range": [1, 10]
        }
    }))
