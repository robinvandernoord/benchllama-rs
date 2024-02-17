import numpy as np
import pandas as pd
from typing import List
from ..constants import (
    PROMPT_EVAL_DURATION,
    PROMPT_EVAL_COUNT,
    EVAL_DURATION,
    EVAL_COUNT,
    PROMPT_EVAL_RATE,
    EVAL_RATE,
)


class ScoreEstimator:
    @staticmethod
    def pass_at_k(n, c, k):
        """
        :param n: total number of samples
        :param c: number of correct samples
        :param k: k in pass@$k$
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    @staticmethod
    def model_task_aggregator(df_group, k):
        n = df_group["result"].count()
        c = df_group["result"].sum()
        passes = {f"pass@{cur_k}": ScoreEstimator.pass_at_k(n, c, cur_k) for cur_k in k}
        return pd.Series(
            {
                PROMPT_EVAL_DURATION: df_group[PROMPT_EVAL_DURATION].mean(),
                PROMPT_EVAL_COUNT: df_group[PROMPT_EVAL_COUNT].mean(),
                EVAL_DURATION: df_group[EVAL_DURATION].mean(),
                EVAL_COUNT: df_group[EVAL_COUNT].mean(),
                **passes,
            }
        )

    @staticmethod
    def model_aggregator(df_group, k):
        return pd.Series(
            {
                PROMPT_EVAL_DURATION: df_group[PROMPT_EVAL_DURATION].mean() / 10**9,
                PROMPT_EVAL_RATE: 10**9
                * df_group[PROMPT_EVAL_COUNT].mean()
                / df_group[PROMPT_EVAL_DURATION].mean(),
                EVAL_DURATION: df_group[EVAL_DURATION].mean() / 10**9,
                EVAL_RATE: 10**9
                * df_group[EVAL_COUNT].mean()
                / df_group[EVAL_DURATION].mean(),
                **{f"pass@{cur_k}": df_group[f"pass@{cur_k}"].mean() for cur_k in k},
            }
        )

    def estimate_score(self, input_df: pd.DataFrame, k: List[int]):
        result_df = (
            input_df.groupby(["model", "task_id", "language"], group_keys=True)
            .apply(ScoreEstimator.model_task_aggregator, k=k)
            .reset_index()
            .groupby(["model", "language"])
            .apply(ScoreEstimator.model_aggregator, k=k)
            .reset_index()
        )

        return result_df
