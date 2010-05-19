Summary:	The GNU Lyric Display System
Name:		lyricue
Version:	2.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.adebenham.com/debian/%{name}_%{version}.tar.gz
URL:		http://www.adebenham.com/lyricue/
Requires:	mysql-client
Requires:	perl-DBD-mysql
Requires:	perl-DBI
Requires:	perl-Gnome2-Canvas
Requires:	perl-Gtk2-GladeXML
Requires:	perl-Gtk2-Spell
Requires:	perl-URI
Suggests:	perl-Gtk2-TrayIcon
Suggests:	perl-Locale-gettext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application is used to edit/display song lyrics and passages of
text on a second screen/projector for use at live events such as
church services, concerts and seminars.

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
%dir %{_sysconfdir}/lyricue
%config(noreplace) %{_sysconfdir}/lyricue/*
%attr(755,root,root) %{_bindir}/lyricue
%attr(755,root,root) %{_bindir}/lyricue_server
%attr(755,root,root) %{_bindir}/lyricue_remote
%attr(755,root,root) %{_bindir}/import_media
%dir %{_datadir}/lyricue
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
%{_datadir}/lyricue/*
%doc %{_docdir}/lyricue/*
%dir %{_docdir}/lyricue
%{_desktopdir}/%{name}*.desktop
