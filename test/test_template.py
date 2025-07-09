import pathlib
from datetime import datetime

import pytest


@pytest.mark.parametrize("template_name", ["foo", "bar"])
def test_template_render(isolated_copy, template_name):
    data = {"template_name": template_name}
    destination: pathlib.Path = isolated_copy(data=data, skip_tasks=False)

    # Ensure the call to copier succeeded and resulted in a valid directory
    assert destination.exists()
    assert destination.is_dir()

    # copier.yml shouold exist in the root of the destination
    assert destination.joinpath("copier.yml"), "copier.yml file was not created"

    # .copier-answers.yml should exist in the root of the destination
    assert destination.joinpath(
        ".copier-answers.yml"
    ).exists(), ".copier-answers.yml file was not created"

    # A LICENSE and NOTICE file should always be present
    assert destination.joinpath("LICENSE").exists(), "LICENSE file was not created"
    assert destination.joinpath("NOTICE").exists(), "NOTICE file was not created"

    # NOTICE file should have the current year injected
    notice_contents = destination.joinpath("NOTICE").read_text()
    assert (
        str(datetime.now().year) in notice_contents
    ), "Current year not found in NOTICE file"


def test_empty_template_name_fails(isolated_copy):
    """Test that an empty template name raises an error."""
    with pytest.raises(ValueError, match="template_name cannot be empty"):
        isolated_copy(data={"template_name": ""}, skip_tasks=False)
