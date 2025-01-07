from click.testing import CliRunner
from primes.main import main

def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.output
