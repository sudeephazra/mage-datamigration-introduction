if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform(*args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        args: The input variables from upstream blocks

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df_user_dtls = args[0]
    df_user_data = args[1]
    df_combined = df_user_data[['userId','title']].merge(df_user_dtls[['id', 'firstname','lastname', 'email']], how='left', left_on='userId', right_on='id').drop(['id'], 1)
    df_combined_ordered = df_combined.reindex(columns=['userId', 'firstname', 'lastname', 'email', 'title'])

    return df_combined_ordered


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
