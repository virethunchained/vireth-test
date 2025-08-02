# main.py – Entry point for Vireth Recursive Learning Engine

from vireth_rle.models.base_model import BaseModel

def main():
    print("Vireth RLE Core Bootstrapping...")
    model = BaseModel()
    model.train()
    print("Execution complete.")

if __name__ == "__main__":
    main()
