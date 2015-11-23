__author__ = 'anthony bell'

import pandas as pd

class MultipleChoiceQuestionLoader():
    def __init__(self, train_file, test_file):
        self.train_df = pd.read_csv(train_file, sep='\t')
        self.sub_df = pd.read_csv(test_file, sep='\t')

    def getMultipleChoiceData(self, df):
        questions = df['question'].values
        answers = df[['answerA', 'answerB', 'answerC', 'answerD']].values
        return zip(questions, answers)

    def getTrainData(self):
        return self.getMultipleChoiceData(self.train_df)

    def getSubmissionData(self):
        return self.getMultipleChoiceData(self.sub_df)