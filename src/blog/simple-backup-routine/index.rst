Simple backup routine
=====================

So I created a
`little backup routine <https://gist.github.com/marceloslacerda/c42a5b3c6d202a23e518bd662ffccc10>`_
for my server. It uses `Dropbox <https://www.dropbox.com>`_ to store an archive
of my server logs and ``/etc``. It simply rsync's the directories excluding old
files, symlinks and empty directories, tar all of it and puts it into a
directory that's synchronized with Dropbox.

All of that is scheduled daily with ``anacron``.

There are two big limitations that I can see so far:

- ``journald`` files are not being sync'd (are journal files readable
  individually?).

  **UPDATE**: Apparently you can point ``journald`` to a directory and it will
  process the logs there.
- It ignores files older than one day but it's only executed when I turn on
  computer on a particular day. So if I don't turn on the computer on a
  certain day, or if on that day the internet is down that backup is not
  stored. I don't think I can do this one without a more serious backup
  solution.

All in all I think this is an OK solution for a small-traffic personal server.