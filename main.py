# Click is a Python package that creates beautiful command line interfaces
import click

# Import PipelineManager class in pipeline_manager in src folder
from src.pipeline_manager import PipelineManager

# Use the following command to excecute the prediction
# python main.py -- train_evaluate_predict_cv --pipeline_name lightGBM

# Create a pipelineManager object named pipeline_manager
pipeline_manager = PipelineManager()

# A group allows a command to have subcommands attached.
# This is the most common way to implement nesting in Click.
@click.group()
# Define function main
def main():
    # The pass statement is used when a statement is required syntactically but you do not want any command or code to execute.
    # The pass statement is a null operation; nothing happens when it executes.
    pass

# click option to create subcommands
@main.command()
@click.option('-p', '--pipeline_name', help='pipeline to be trained', required=True)
@click.option('-d', '--dev_mode', help='if true only a small sample of data will be used', is_flag=True, required=False)
def train(pipeline_name, dev_mode):
    pipeline_manager.train(pipeline_name, dev_mode)


@main.command()
@click.option('-p', '--pipeline_name', help='pipeline to be trained', required=True)
@click.option('-d', '--dev_mode', help='if true only a small sample of data will be used', is_flag=True, required=False)
def evaluate(pipeline_name, dev_mode):
    pipeline_manager.evaluate(pipeline_name, dev_mode)


@main.command()
@click.option('-p', '--pipeline_name', help='pipeline to be trained', required=True)
@click.option('-d', '--dev_mode', help='if true only a small sample of data will be used', is_flag=True, required=False)
@click.option('-s', '--submit_predictions', help='submit predictions if true', is_flag=True, required=False)
def predict(pipeline_name, dev_mode, submit_predictions):
    pipeline_manager.predict(pipeline_name, dev_mode, submit_predictions)


@main.command()
@click.option('-p', '--pipeline_name', help='pipeline to be trained', required=True)
@click.option('-s', '--submit_predictions', help='submit predictions if true', is_flag=True, required=False)
@click.option('-d', '--dev_mode', help='if true only a small sample of data will be used', is_flag=True, required=False)
def train_evaluate_predict(pipeline_name, submit_predictions, dev_mode):
    pipeline_manager.train(pipeline_name, dev_mode)
    pipeline_manager.evaluate(pipeline_name, dev_mode)
    pipeline_manager.predict(pipeline_name, dev_mode, submit_predictions)


@main.command()
@click.option('-p', '--pipeline_name', help='pipeline to be trained', required=True)
@click.option('-d', '--dev_mode', help='if true only a small sample of data will be used', is_flag=True, required=False)
def train_evaluate(pipeline_name, dev_mode):
    pipeline_manager.train(pipeline_name, dev_mode)
    pipeline_manager.evaluate(pipeline_name, dev_mode)


@main.command()
@click.option('-p', '--pipeline_name', help='pipeline to be trained', required=True)
@click.option('-s', '--submit_predictions', help='submit predictions if true', is_flag=True, required=False)
@click.option('-d', '--dev_mode', help='if true only a small sample of data will be used', is_flag=True, required=False)
def evaluate_predict(pipeline_name, submit_predictions, dev_mode):
    pipeline_manager.evaluate(pipeline_name, dev_mode)
    pipeline_manager.predict(pipeline_name, dev_mode, submit_predictions)


@main.command()
@click.option('-p', '--pipeline_name', help='pipeline to be trained', required=True)
@click.option('-l', '--model_level', help='level of modeling first or second are available', default='first',
              required=True)
@click.option('-d', '--dev_mode', help='if true only a small sample of data will be used', is_flag=True, required=False)
def train_evaluate_cv(pipeline_name, model_level, dev_mode):
    pipeline_manager.train_evaluate_cv(pipeline_name, model_level, dev_mode)


@main.command()
@click.option('-p', '--pipeline_name', help='pipeline to be trained', required=True)
@click.option('-l', '--model_level', help='level of modeling first or second are available', default='first',
@click.option('-s', '--submit_predictions', help='submit predictions if true', is_flag=True, required=False)
              required=True)
@click.option('-d', '--dev_mode', help='if true only a small sample of data will be used', is_flag=True, required=False)

# Train Evaluate Predict Cross-Validate
# train_evaluate_predict_cv('lightGBM','first',True,True)
def train_evaluate_predict_cv(pipeline_name, model_level, dev_mode, submit_predictions):
    # this function in pipeline_manager is excecuted when using option train_evaluate_predict_cv
    pipeline_manager.train_evaluate_predict_cv(pipeline_name, model_level, dev_mode, submit_predictions)

if __name__ == "__main__":
    main()
