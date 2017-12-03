Unlocking yourself out of a dead boot
=====================================

This morning I was presented with an annoying situation with my ``debian``
installation: ``systemd`` tried to boot, since there was some failures mounting
some partitions it aborted the boot process and tried to drop to a root shell,
but since the root account was locked ``systemd`` shrugged and gave up the whole
process leaving me with an unfixable system.
`This is a known bug by the way <https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=789950>`_.

I tried using the shell from the install CD but it doesnt have the crypto
tools to mount my root (because it’s encrypted :^).

I imagined that there had to be some ``GRUB`` boot option to force ``systemd`` to
ignore all errors and continue with the boot. I wasn't able to find that but I
got something that enabled me to solve the problem:

#. Whenever the ``GRUB`` screen appear press "``e``" to edit the entry.
#. Go to the kernel boot line like the following::

    linux   /vmlinuz-4.9.0-2-amd64 root=/dev/mapper/fedora-00 ro single iommu=soft

#. And do the these:

  a) Change "``ro``" to "``rw``" to allow you to make changes to the filesystem.
  b) Append "``init=/bin/sh``" to the line so the kernel will drop to a shell instead of running ``systemd``.
  c) Boot with that configuration(by either pressing ``Ctrl+x`` or ``F10``)
  d) Once you are logged in use ``vi`` to edit ``/etc/fstab``.
  e) Comment the lines that are causing the problem, or use the ``nofail``
     option as explained `here <https://bbs.archlinux.org/viewtopic.php?pid=1149895#p1149895>`_.
  f) Reboot the machine normally.
