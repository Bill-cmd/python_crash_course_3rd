def print_models(unprinted_desings, complated_models):
    """
    模拟打印每个设计，指导没有未打印的设计为止
    打印每个设计后，都将其移到列表 complated_models 中
    """
    while unprinted_desings:
        current_design = unprinted_desings.pop()
        print(f"Printing model: {current_design}")
        complated_models.append(current_design)


def show_complated_models(complated_models):
    """显示打印好的所有模型"""
    print(f"\nThe following models have been printed:")
    for complated_model in complated_models:
        print(complated_model)

