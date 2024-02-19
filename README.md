# 👀 See it in action

# `benchllama`

**Usage**:

```console
$ benchllama [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `clean`
- `evaluate`

## `benchllama clean`

**Usage**:

```console
$ benchllama clean [OPTIONS]
```

**Options**:

- `--run-id TEXT`: Run id
- `--output PATH`: Output directory [default: /tmp]
- `--help`: Show this message and exit.

## `benchllama evaluate`

**Usage**:

```console
$ benchllama evaluate [OPTIONS]
```

**Options**:

- `--models TEXT`: Names of models that need to be evaluated. [required]
- `--provider-url TEXT`: The endpoint of the model provider. [default: http://localhost:11434]
- `--dataset FILE`: By default, bigcode/humanevalpack from Hugging Face will be used. If you want to use your own dataset, specify the path here.
- `--languages [python|js|java|go|cpp]`: List of languages to evaluate from bigcode/humanevalpack. Ignore this if you are brining your own data [default: Language.python]
- `--num-completions INTEGER`: Number of completions to be generated for each task. [default: 3]
- `--k INTEGER`: The k for calculating pass@k. The values shouldn't exceed num_completions [default: 1, 2]
- `--samples INTEGER`: Number of dataset samples to evaluate. By default, all the samples get processed. [default: -1]
- `--output PATH`: Output directory [default: /tmp]
- `--help`: Show this message and exit.
