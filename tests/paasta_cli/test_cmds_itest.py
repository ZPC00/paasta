from mock import MagicMock
from mock import patch

from paasta_tools.paasta_cli.cmds.itest import paasta_itest


@patch('paasta_tools.paasta_cli.cmds.itest.validate_service_name', autospec=True)
@patch('paasta_tools.paasta_cli.cmds.itest._run', autospec=True)
@patch('sys.exit')
@patch('paasta_tools.paasta_cli.cmds.itest.check_docker_image', autospec=True)
def test_itest_run_fail(
    mock_docker_image,
    mock_exit,
    mock_run,
    mock_validate_service_name,
):
    mock_docker_image.return_value = True
    mock_run.return_value = (1, 'fake_output')
    args = MagicMock()
    paasta_itest(args)
    mock_exit.assert_called_once_with(1)


@patch('paasta_tools.paasta_cli.cmds.itest.validate_service_name', autospec=True)
@patch('paasta_tools.paasta_cli.cmds.itest._run', autospec=True)
@patch('paasta_tools.paasta_cli.cmds.itest.check_docker_image', autospec=True)
def test_itest_success(
    mock_docker_image,
    mock_run,
    mock_validate_service_name,
):
    mock_docker_image.return_value = True
    mock_run.return_value = (0, 'Yeeehaaa')

    args = MagicMock()
    assert paasta_itest(args) is None


@patch('paasta_tools.paasta_cli.cmds.itest.validate_service_name', autospec=True)
@patch('paasta_tools.paasta_cli.cmds.itest._run', autospec=True)
@patch('paasta_tools.paasta_cli.cmds.itest.build_docker_tag', autospec=True)
@patch('paasta_tools.paasta_cli.cmds.itest.check_docker_image', autospec=True)
def test_itest_works_when_service_name_starts_with_services_dash(
    mock_docker_image,
    mock_build_docker_tag,
    mock_run,
    mock_validate_service_name,
):
    mock_docker_image.return_value = True
    mock_build_docker_tag.return_value = 'unused_docker_tag'
    mock_run.return_value = (0, 'Yeeehaaa')
    args = MagicMock()
    args.service = 'services-fake_service'
    args.commit = 'unused'
    assert paasta_itest(args) is None
    mock_build_docker_tag.assert_called_once_with('fake_service', 'unused')
