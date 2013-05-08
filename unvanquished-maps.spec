%define debug_package	%{nil}
%define oname Unvanquished
Name:           unvanquished-maps
Version:        0.15.0
Release:        1
Summary:        Sci-fi RTS and FPS game
License:        CC-BY-SA-2.5 and CC-BY-SA-3.0
Group:          Games/Arcade
Url:            http://unvanquished.net/
#obtaining the sources:
#http://sourceforge.net/projects/unvanquished/files/Map%20Pack/
Source0:        unvanquished-maps-0.15.0.tar.bz2
BuildArch:      noarch
Requires:       unvanquished == %{version}

%description
Players fight online in team based combat in a war of aliens against humans.

This package only contains the map pack.

%prep
%setup -q 

%build

%install
mkdir -p  %{buildroot}%{_datadir}/%{oname}/main/
install -m0644 {map-arachnid2-gpp,map-atcshd-gpp2,map-atcszalpha-b2,map-bluedragon2_b3,map-citadel,map-cruz-b6,map-Eden-b3,map-karith-gpp,map-methane-beta1,map-nano,map-nexus6-gpp,map-niveus-gpp,map-orion-beta2,map-perseus-b3,map-plat23-b3,map-procyon-r1,map-sirius,map-spacetracks-r1,map-station15-r1,map-transit-gpp,map-tremor-gpp,map-UTCSfinal,map-veddak-final,map-wrecktify_b2}.pk3 %{buildroot}%{_datadir}/%{oname}/main/

%files
%{_datadir}/%{oname}/main/*.pk3

