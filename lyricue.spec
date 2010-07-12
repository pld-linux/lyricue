
%include    /usr/lib/rpm/macros.perl

Summary:	GNU Lyric Display System, client interface
Name:		lyricue
Version:	2.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.lyricue.org/archive/%{name}_%{version}.tar.gz
# Source0-md5:	30fe4d6c32c8082addc2e50c12363425
URL:		http://www.lyricue.org
BuildRequires:	gettext-devel
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
Requires:	%{name}-remote
Requires:	%{name}-server
Requires:	mysql-client
Requires:	perl-Gtk2 >= 1.220
Suggests:	diatheke
Suggests:	mysql
Suggests:	perl-Clutter
Suggests:	perl-Clutter-GStreamer
Suggests:	perl-DBD-mysql
Suggests:	perl-DBD-mysql
Suggests:	perl-DBD-SQLite
Suggests:	perl-Gtk2-Clutter
Suggests:	perl-Gtk2-Spell
Suggests:	perl-Gtk2-TrayIcon
Suggests:	totem
Suggests:	unoconv
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lyricue is used to edit and display song lyrics and passages of text
along with images and videos on a second screen/projector. It was
designed for use at live events such as church services, concerts and
seminars.

%package server
Summary:	GNU Lyric Display System, server interface
Group:		X11/Applications/Graphics
Requires:	perl-Gtk2 >= 1.220
Suggests:	perl-Clutter
Suggests:	perl-Clutter-GStreamer
Suggests:	perl-DBD-mysql
Suggests:	perl-DBD-SQLite
Suggests:	perl-Gtk2-Clutter
Suggests:	perl-Locale-gettext
Suggests:	totem

%description server
Component to handle action display and projection of slides.

%package remote
Summary:	GNU Lyric Display System, remote control cli
Group:		Libraries

%description remote
Remote control CLI to control the projection server from any shell.

%prep
%setup -q

# Fix perl shebang
%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' %{name} %{name}_server %{name}_remote

# Fix Spanish language code
%{__sed} -e 's#po/es_ES#po/es#' -i Makefile
mv debian/po/es{_ES,}.po

# Fix issue with use of deprecated method in Gtk2, fixed in cvs upstream
%{__sed} -i -e 's!Gtk2::Gdk::Color->from_string!Gtk2::Gdk::Color->parse!' %{name}_server

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/access.conf{.example,}
rm -r $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/import_media
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_desktopdir}/%{name}.desktop

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}_server
%{_desktopdir}/%{name}_server.desktop

%files remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}_remote
