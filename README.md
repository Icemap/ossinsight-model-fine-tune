# OSSInsight Model Fine Tune

## How to use it?

> **Note:**
>
> You can get more infomation at the [OpneAI document](https://beta.openai.com/docs/guides/fine-tuning).

- Get a fine tune data file by `fine-tune-data` folder, and you will get two files, its named `fine_tune.jsonl`(output by python script) and `fine_tune_prepared.jsonl`(checked and transferred by openai tools).

    ```shell
    make data
    ```

- Set your OpenAI API Key and create your new model.

    ```shell
    export OPENAI_API_KEY="<OPENAI_API_KEY>"
    openai api fine_tunes.create -t fine_tune_prepared.jsonl -m davinci --suffix 'ossinsight'
    ```

    And you will get output like this, the fine-tune job ID in it:

    ```shell
    $ openai api fine_tunes.create -t fine_tune_prepared.jsonl -m davinci --suffix 'ossinsight'
    Upload progress: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 941/941 [00:00<00:00, 706kit/s]
    Uploaded file from fine_tune_prepared.jsonl: file-YxUZUtd4EO9aGYHLgR0wsPVg
    Created fine-tune: ft-i4L7Jm7W2UXAKMKC1vgk5Fz4
    Streaming events until fine-tuning is complete...

    (Ctrl-C will interrupt the stream, but not cancel the fine-tune)
    [2023-01-02 03:53:54] Created fine-tune: ft-i4L7Jm7W2UXAKMKC1vgk5Fz4
    [2023-01-02 03:54:36] Fine-tune costs $0.05
    [2023-01-02 03:54:36] Fine-tune enqueued. Queue number: 0
    [2023-01-02 03:54:37] Fine-tune started

    Stream interrupted (client disconnected).
    To resume the stream, run:

      openai api fine_tunes.follow -i ft-i4L7Jm7W2UXAKMKC1vgk5Fz4
    ```

    So, in this case, the job ID is `ft-i4L7Jm7W2UXAKMKC1vgk5Fz4`.

- Monitor this job ID:

    ```shell
    openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
    ```

    In this case, the command is:

    ```shell
    openai api fine_tunes.follow -i ft-i4L7Jm7W2UXAKMKC1vgk5Fz4
    ```

    And you will get output like this, the model ID in it:

    ```shell
    openai api fine_tunes.follow -i ft-i4L7Jm7W2UXAKMKC1vgk5Fz4
    [2023-01-02 03:53:54] Created fine-tune: ft-i4L7Jm7W2UXAKMKC1vgk5Fz4
    [2023-01-02 03:54:36] Fine-tune costs $0.05
    [2023-01-02 03:54:36] Fine-tune enqueued. Queue number: 0
    [2023-01-02 03:54:37] Fine-tune started
    [2023-01-02 03:55:58] Completed epoch 1/4
    [2023-01-02 03:56:00] Completed epoch 2/4
    [2023-01-02 03:56:01] Completed epoch 3/4
    [2023-01-02 03:56:03] Completed epoch 4/4
    [2023-01-02 03:57:10] Uploaded model: davinci:ft-personal:ossinsight-2023-01-01-19-57-09
    [2023-01-02 03:57:11] Uploaded result file: file-lddf9E3Kdc7lB3jbxQtW7OmF
    [2023-01-02 03:57:12] Fine-tune succeeded

    Job complete! Status: succeeded 🎉
    Try out your fine-tuned model:

    openai api completions.create -m davinci:ft-personal:ossinsight-2023-01-01-19-57-09 -p <YOUR_PROMPT>
    ```

    So, in this case, the model ID is `davinci:ft-personal:ossinsight-2023-01-01-19-57-09`.

- Then, you can use the model by ID in your own OSSInsight.

## How can I add a case in the fine-tune data?

- Add a folder in the `fine-tune-data` folder (For example, it's named `test-data`).
- Add two files, named `prompt` and `completion`. Basically speaking, the `prompt` is a question, and the `completion` is the corresponding correct answer.
- [Give a PR](https://github.com/Icemap/ossinsight-model-fine-tune/pulls), waiting for merge, that's all.
