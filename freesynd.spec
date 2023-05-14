Name:		freesynd
Version:	0.7.5
Release:	1
Summary:	Open-source engine for the classic DOS game Syndicate
Group:		Games/Strategy
License:	GPLv2
URL:		http://freesynd.sourceforge.net/
Source0:	http://sourceforge.net/projects/freesynd/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		freesynd-0.7-path.patch
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(zlib)

%description
FreeSynd is a cross-platform, GPLed reimplementation of engine for the classic
Bullfrog game, Syndicate.

Syndicate is an isometric real-time tactical game created in 1993.

Gameplay involves ordering a four-person team of cyborg agents around cities
displayed in a fixed-view isometric style, in pursuit of mission goals such
as assassinating executives of a rival syndicate, rescuing captured allies,
"persuading" civilians and scientists to join the player's company or simply
killing all enemy agents.

As the player progresses through the game, they must manage the research and
development of new weaponry and cyborg upgrades. The player has only limited
funds, requiring taxation of the conquered territories while ensuring that
they are not so over-taxed that they revolt against the player.

WARNING!!! You need original game data to play this game. Copy all files from
data directory to: %{_gamesdatadir}/%{name}/data/

%prep
%setup -q
%patch0 -p1
for N in 16 32 64 128; do convert icon/sword.png -resize ${N}x${N} $N.png; done

%build
%cmake -DCMAKE_BUILD_TYPE=release
%make

%install
%makeinstall_std -C build

install -D 16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D 32.png %{buildroot}%{_liconsdir}/%{name}.png
install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Syndicate (freesynd)
Comment=An isometric real-time tactical game
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%files
%doc AUTHORS COPYING NEWS README
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

