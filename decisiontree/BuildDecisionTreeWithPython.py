import numpy as np

eps = np.finfo(float).eps
print('eps is : ',eps)

def find_entropy_of_set(data_set):
    target_var = data_set.keys()[-1]
    entropy = 0
    values = data_set[target_var].unique()
    for value in values:
        fraction = data_set[target_var].value_counts()[value] / len(data_set[target_var])
        entropy += -fraction * np.log2(fraction)
    return entropy


def find_total_entropy_of_attribute(df, attribute):
    target_var = df[df.keys()[-1]].unique()
    in_scope_var = df[attribute].unique()
    entropy_var_sum = 0

    for variable in in_scope_var:
        entropy = 0
        for target_variable in target_var:
            num = len(df[attribute][df[attribute] == variable][df[df.keys()[-1]] == target_variable])
            den = len(df[attribute][df[attribute] == variable])
            fraction = num / (den + eps)
            entropy += -fraction * np.log2(fraction + eps)
        fraction2 = den / len(df)
        entropy_var_sum += -fraction2 * entropy
    return abs(entropy_var_sum)


def find_max_information_gain_attribute(df):
    attributes_except_target = df.keys()[:-1]
    information_gain_all = []
    for key in attributes_except_target:
        information_gain = find_entropy_of_set(df) - find_total_entropy_of_attribute(df, key)
        information_gain_all.append(information_gain)
    return attributes_except_target[np.argmax(information_gain_all)]


def get_subset_of_data(df, attribute, value):
    return df[df[attribute] == value].reset_index(drop=True)


def build_decision_tree(df, tree=None):
    max_ig_attribute = find_max_information_gain_attribute(df)
    selected_attr_uniq_values = np.unique(df[max_ig_attribute])

    if tree is None:
        tree = {}
        tree[max_ig_attribute] = {}

    for value in selected_attr_uniq_values:
        subset = get_subset_of_data(df, max_ig_attribute, value)
        attr_value, counts = np.unique(subset['PlayTennis'], return_counts=True)
        if len(counts) == 1:
            tree[max_ig_attribute][value] = attr_value[0]
        else:
            tree[max_ig_attribute][value] = build_decision_tree(subset)
    return tree


def predict_the_values(new_data, tree):
    for key in tree.keys():
        value = new_data[key]
        tree = tree[key][value]
        prediction = 0
        if type(tree) is dict:
            prediction = predict_the_values(new_data, tree)
        else:
            prediction = tree
            break;
    return prediction
