from pathlib import Path
from acautils import standard_log, version_handler


class TestVersion:
    def test_version(self, poetry_version):
        """
        - WHEN the get_version script is called
        - GIVEN it has been imported into a new module (here the test module)
        - THEN it should be able to find the version in the .toml file and it should be the same as the one the native poetry process returns
        """
        VH_version: str = version_handler.get_version(Path("pyproject.toml").absolute())
        assert VH_version in poetry_version

    # TODO: Currently does not work. I have not found a way to set the __file__ variable via monkey patch
    # def test_version_fail(self, monkeypatch, tmp_path):
    #     """
    #     - WHEN the get version script is called
    #     - GIVEN a path where there is no way to get a pyproject.toml file
    #     - THEN should return 'Unknown version'
    #     """
    #     monkeypatch.setenv(__file__, tmp_path)
    #     VH_version: str = version_handler.get_version()
    #     assert VH_version == 'Unknown version'


class TestLog:
    def test_log(self, tmp_path):
        """
        - WHEN a new log is made
        - GIVEN the path to the tmp_path
        - THEN a log should be made in the dir
        """
        standard_log.setup_logger(tmp_path, "test")
        log_path: Path = tmp_path / "_metadata" / "test.log"
        assert log_path.exists()
