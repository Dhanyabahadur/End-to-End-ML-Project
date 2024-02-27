import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    ## Note: You can add different data transformation techniques such as Scaler, PCA and others
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model
        

    # I am only adding train_test_split here
        

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        all_cols = list(data.columns)
        all_cols = [i for i in all_cols if i != 'Id']
        data = data[all_cols].copy()

        # split the data into training and test sets. (0.75, 0.25) split
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

