# TODO:
# - Split packages for core, client and remote
# - Add default access.conf file to package
Summary:	GNU Lyric Display System, client interface
Name:		lyricue
Version:	2.0.0
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.adebenham.com/debian/%{name}_%{version}.tar.gz
# Source0-md5:	cd0fb1c9b0e6ccadc52cda2601b86be6
URL:		http://www.lyricue.org
Requires:	diatheke
Requires:	mysql-client
Requires:	perl-DBD-mysql
Requires:	perl-DBI
Requires:	perl-Gnome2-Canvas
Requires:	perl-GStreamer
Requires:	perl-Gtk2-GladeXML
Requires:	perl-Gtk2-Spell
Requires:	perl-Locale-gettext
Requires:	perl-URI
Suggests:	perl-Gtk2-TrayIcon
Suggests:	%{name}-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lyricue is used to edit and display song lyrics and
passages of text along with images and videos on a second
screen/projector. It was designed for use at live events
such as church services, concerts and seminars.

%package server
Summary:	GNU Lyric Display System, server interface 
Group:		X11/Applications/Graphics
Requires:	perl-GStreamer
Requires:	perl-Locale-gettext

%description server
Component to handle action display and projection of slides.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/lyricue_remote
%attr(755,root,root) %{_bindir}/import_media
%dir %{_datadir}/%{name}
%lang(en_US) %dir %{_datadir}/locale/en_US
%lang(en_US) %dir %{_datadir}/locale/en_US/LC_MESSAGES
%lang(en_US) %{_datadir}/locale/en_US/LC_MESSAGES/lyricue.mo
%lang(es_ES) %dir %{_datadir}/locale/es_ES
%lang(es_ES) %dir %{_datadir}/locale/es_ES/LC_MESSAGES
%lang(es_ES) %{_datadir}/locale/es_ES/LC_MESSAGES/lyricue.mo
%lang(de) %dir %{_datadir}/locale/de
%lang(de) %dir %{_datadir}/locale/de/LC_MESSAGES
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/lyricue.mo
%lang(fr) %dir %{_datadir}/locale/fr
%lang(fr) %dir %{_datadir}/locale/fr/LC_MESSAGES
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/lyricue.mo
%lang(nl) %dir %{_datadir}/locale/nl
%lang(nl) %dir %{_datadir}/locale/nl/LC_MESSAGES
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/lyricue.mo
%lang(sv) %dir %{_datadir}/locale/sv
%lang(sv) %dir %{_datadir}/locale/sv/LC_MESSAGES
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/lyricue.mo
%{_datadir}/%{name}/*
%{_desktopdir}/%{name}.desktop
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%files server
%attr(755,root,root) %{_bindir}/%{name}_server
%{_desktopdir}/%{name}_server.desktop
