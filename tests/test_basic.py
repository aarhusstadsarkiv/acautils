from pathlib import Path
from acautils import standard_log, version_handler


class TestVersion:

    def test_version(self, poetry_version):
        """
        - WHEN the get_version script is called
        - GIVEN it has been imported into a new module (here the test module)
        - THEN it should be able to find the version in the .toml file and it should be the same as the one the native poetry process returns
        """
        VH_version: str = version_handler.get_version()
        assert VH_version in poetry_version


    def test_version_fail(self):
        """
        - WHEN the get version script is called
        - GIVEN a path where there is no way to get a pyproject.toml file
        - THEN should return 'Unknown version'
        """
        VH_version: str = version_handler.get_version(Path("C:\\Users\\az65716\\GitHub"))
        assert VH_version == 'Unknown version'


class TestLog:

    def test_log(self, tmp_path):
        """
        - WHEN a new log is made
        - GIVEN the path to the tmp_path
        - THEN a log should be made in the dir with the version of the tool as its first line
        """
        standard_log.setup_logger(tmp_path, "test")
        log_path: Path = tmp_path / "_metadata" / "test.log"
        assert log_path.exists()
        first_line: str = log_path.read_text()
        assert version_handler.get_version() in first_line
