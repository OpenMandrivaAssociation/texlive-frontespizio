%global tl_name frontespizio
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4a
Release:	%{tl_revision}.1
Summary:	Create a frontispiece for Italian theses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/frontespizio
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frontespizio.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frontespizio.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frontespizio.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typesetting a frontispiece independently of the layout of the main
document is difficult. This package provides a solution by producing an
auxiliary TeX file to be typeset on its own and the result is
automatically included at the next run. The markup necessary for the
frontispiece is written in the main document in a frontespizio
environment. Documentation is mainly in Italian, as the style is
probably apt only to theses in Italy.

