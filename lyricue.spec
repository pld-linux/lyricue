# TODO:
# - Split packages for core, client and remote
Summary:	GNU Lyric Display System, client interface
Name:		lyricue
Version:	2.0.0
Release:	8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.adebenham.com/debian/%{name}_%{version}.tar.gz
# Source0-md5:	cd0fb1c9b0e6ccadc52cda2601b86be6
URL:		http://www.lyricue.org
Patch0:		%{name}-shebang.patch
BuildRequires:	rpm-perlprov
Requires:	mysql-client
Suggests:	%{name}-server
Suggests:	diatheke
Suggests:	mysql
Suggests:	perl(DBD::mysql)
Suggests:	perl(Gtk2::TrayIcon)
Suggests:	unoconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lyricue is used to edit and display song lyrics and passages of text
along with images and videos on a second screen/projector. It was
designed for use at live events such as church services, concerts and
seminars.

%package server
Summary:	GNU Lyric Display System, server interface
Group:		X11/Applications/Graphics
BuildRequires:	rpm-perlprov
Suggests:	perl(DBD::mysql)
Suggests:	perl(Locale::gettext)

%description server
Component to handle action display and projection of slides.

%prep
%setup -q
%patch0 -p0

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
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}_remote
%attr(755,root,root) %{_bindir}/import_media
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_desktopdir}/%{name}.desktop

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}_server
%{_desktopdir}/%{name}_server.desktop
