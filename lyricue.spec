# TODO:
# - Make sure server subpackage can run without the client

%include    /usr/lib/rpm/macros.perl

Summary:	GNU Lyric Display System, client interface
Name:		lyricue
Version:	2.0.0
Release:	0.11
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.adebenham.com/debian/%{name}_%{version}.tar.gz
# Source0-md5:	cd0fb1c9b0e6ccadc52cda2601b86be6
Patch0:		%{name}-perlshebang.patch
URL:		http://www.lyricue.org
BuildRequires:	gettext-devel
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
Requires:	mysql-client
Suggests:	%{name}-server
Suggests:	%{name}-remote
Suggests:	diatheke
Suggests:	mysql
Suggests:	perl(Clutter)
Suggests:	perl(DBD::mysql)
Suggests:	perl(Gtk2::TrayIcon)
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
Suggests:	perl(Clutter)
Suggests:	perl(DBD::mysql)
Suggests:	perl(Locale::gettext)

%description server
Component to handle action display and projection of slides.

%package remote
Summary:	GNU Lyric Display System, remote control cli
Group:	Libraries

%description remote
Remote control CLI to control the projection server from any shell.

%prep
%setup -q
%patch0 -p0

sed -e 's#po/es_ES#po/es#' -i Makefile
mv po/es{_ES,}.po

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/access.conf{.example,}

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
