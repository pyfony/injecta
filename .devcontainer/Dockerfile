FROM python:3.5

# Copy default endpoint specific user settings overrides into container to specify Python path
COPY .devcontainer/settings.vscode.json /root/.vscode-remote/data/Machine/settings.json

RUN apt-get update && apt-get -y install git procps libicu[0-9][0-9]

WORKDIR /workspace

COPY .devcontainer/requirements.txt requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt

ENV PYTHONPATH /workspaces/injecta/src

ENV PYTHONDONTWRITEBYTECODE=1

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
