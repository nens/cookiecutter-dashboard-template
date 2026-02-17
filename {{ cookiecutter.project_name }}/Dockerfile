FROM python:3.14-trixie
WORKDIR /code
LABEL project_name="{{ cookiecutter.project_name }}"

# Install python stuff with uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock ./
RUN uv sync
# Add the virtualenv to the path so that calling "streamlit" just works.
ENV PATH="/code/.venv/bin:$PATH"

# Copy the rest of our code. Contents mentioned in .dockerignore are ignored.
COPY . .

# Run streamlit
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
