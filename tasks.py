import os
from dotenv import load_dotenv
from invoke import task
from subprocess import call
from sys import platform

load_dotenv()

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def reset_db(ctx):
    ctx.run("python3 src/db_helper.py", pty=True)


@task
def autopep(ctx):
    ctx.run("autopep8 --in-place --recursive .", pty=True)


@task
def open_db(ctx):
    url = os.environ.get("DATABASE_URL")
    ctx.run(f'psql "{url}"', pty=True)


@task
def test(ctx):
    ctx.run("pytest", pty=True)


@task
def robot(ctx):
    ctx.run("robot src/story_tests", pty=True)


@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest; coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))