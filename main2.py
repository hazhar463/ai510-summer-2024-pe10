from cityu_pack.sub_class_pack.class_module import ClassModule
from cityu_pack.sub_func_pack.func_module import multiply as func_multiply

def main():
    # ClassModule example
    cm = ClassModule(global_init_param=5)
    class_result = cm.multiply(3)
    print(f"ClassModule multiply result: {class_result}")

    # Function example
    func_result = func_multiply(4, 2)
    print(f"Function multiply result: {func_result}")

if __name__ == "__main__":
    main()