from plumbum.cmd import git


def check_git_unchanged(filename, yes=False):
    """Check git to avoid overwriting user changes."""
    if check_staged(filename):
        s = f'There are staged changes in {filename}, overwrite? [y/n] '
        if yes or input(s) in ('y', 'yes'):
            return
        else:
            raise RuntimeError('There are staged changes in '
                               '{}, aborting.'.format(filename))
    if check_unstaged(filename):
        s = f'There are unstaged changes in {filename}, overwrite? [y/n] '
        if yes or input(s) in ('y', 'yes'):
            return
        else:
            raise RuntimeError('There are unstaged changes in '
                               '{}, aborting.'.format(filename))


def check_staged(filename=None):
    """Check if there are 'changes to be committed' in the index."""
    retcode, _, stdout = git['diff-index', '--quiet', '--cached', 'HEAD',
                             filename].run(retcode=None)
    if retcode == 1:
        return True
    elif retcode == 0:
        return False
    else:
        raise RuntimeError(stdout)


def check_unstaged(filename):
    """Check if there are 'changes not staged for commit' in the working
    directory.
    """
    retcode, _, stdout = git['diff-files', '--quiet',
                             filename].run(retcode=None)
    if retcode == 1:
        return True
    elif retcode == 0:
        return False
    else:
        raise RuntimeError(stdout)
