import json

def main():
    train_annotation_path = "GAIC-Text-Annotations/train.json"
    with open(train_annotation_path, "r") as f:
        train_annotation = json.load(f)
        # print number of annotations
        print('number of annotations in train set:', len(train_annotation))
        # print first annotation
        print('first annotation:', list(train_annotation.items())[0])
    
    validation_annotation_path = "GAIC-Text-Annotations/valid.json"
    with open(validation_annotation_path, "r") as f:
        validation_annotation = json.load(f)
        # print number of annotations
        print('number of annotations in validation set:', len(validation_annotation))
        # print first annotation
        print('first annotation:', list(validation_annotation.items())[0])
    
    test_annotation_path = "GAIC-Text-Annotations/test.json"
    with open(test_annotation_path, "r") as f:
        test_annotation = json.load(f)
        # print number of annotations
        print('number of annotations in test set:', len(test_annotation))
        # print first annotation
        print('first annotation:', list(test_annotation.items())[0])

if __name__ == "__main__":
    main()