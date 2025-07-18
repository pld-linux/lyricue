# TODO:
# - Make sure display and remote subpackages can run without the client


Summary:	GNU Lyric Display System, client interface
Name:		lyricue
Version:	3.6.5
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.lyricue.org/archive/%{name}_%{version}.tar.gz
# Source0-md5:	e4646b89cee70f05c11f6362a27f369a
Patch0:		%{name}-gstreamer.patch
URL:		http://www.lyricue.org
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
Requires:	%{name}-display = %{version}-%{release}
Requires:	%{name}-remote = %{version}-%{release}
Requires:	mysql-client
Requires:	perl-Gtk2 >= 1.220
Requires:	perl-Net-Bonjour
Requires:	perl-Net-Rendezvous-Publish
Suggests:	ImageMagick
Suggests:	diatheke
Suggests:	mysql
Suggests:	perl-DBD-mysql
Suggests:	perl-Gtk2-Spell
Suggests:	perl-Gtk2-TrayIcon
Suggests:	totem
Suggests:	unoconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lyricue is used to edit and display song lyrics and passages of text
along with images and videos on a second screen/projector. It was
designed for use at live events such as church services, concerts and
seminars.

%package display
Summary:	GNU Lyric Display System, display interface
Group:		X11/Applications/Graphics
Requires:	perl-Gtk2 >= 1.220
Suggests:	perl-DBD-mysql
Suggests:	perl-Locale-gettext
Suggests:	totem
Obsoletes:	lyricue-server

%description display
Component to handle action display and projection of slides.

%package remote
Summary:	GNU Lyric Display System, remote control cli
Group:		Libraries

%description remote
Remote control CLI to control the projection display from any shell.

%prep
%setup -q
%patch -P0 -p0

# Fix perl shebang
%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' src/%{name} src/%{name}_remote

%build
%configure \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_desktopdir}/%{name}.desktop

%files display
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}_display
%{_desktopdir}/%{name}_display.desktop

%files remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}_remote
