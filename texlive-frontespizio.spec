Name:		texlive-frontespizio
Version:	24054
Release:	2
Summary:	Create a frontispiece for Italian theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/frontespizio
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frontespizio.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frontespizio.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frontespizio.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typesetting a frontispiece independently of the layout of the
main document is difficult. This package provides a solution by
producing an auxiliary TeX file to be typeset on its own and
the result is automatically included at the next run. The
markup necessary for the frontispiece is written in the main
document in a frontespizio environment. Documentation is mainly
in Italian, as the style is probably apt only to theses in
Italy.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/frontespizio/frontespizio.sty
%doc %{_texmfdistdir}/doc/latex/frontespizio/README
%doc %{_texmfdistdir}/doc/latex/frontespizio/examplea.pdf
%doc %{_texmfdistdir}/doc/latex/frontespizio/examplea.tex
%doc %{_texmfdistdir}/doc/latex/frontespizio/exampleasuf.pdf
%doc %{_texmfdistdir}/doc/latex/frontespizio/exampleasuf.tex
%doc %{_texmfdistdir}/doc/latex/frontespizio/exampleb.pdf
%doc %{_texmfdistdir}/doc/latex/frontespizio/exampleb.tex
%doc %{_texmfdistdir}/doc/latex/frontespizio/examplec.pdf
%doc %{_texmfdistdir}/doc/latex/frontespizio/examplec.tex
%doc %{_texmfdistdir}/doc/latex/frontespizio/exampled.pdf
%doc %{_texmfdistdir}/doc/latex/frontespizio/exampled.tex
%doc %{_texmfdistdir}/doc/latex/frontespizio/examplee.pdf
%doc %{_texmfdistdir}/doc/latex/frontespizio/examplee.tex
%doc %{_texmfdistdir}/doc/latex/frontespizio/fakelogo.mp
%doc %{_texmfdistdir}/doc/latex/frontespizio/fakelogo.pdf
%doc %{_texmfdistdir}/doc/latex/frontespizio/frontespizio.pdf
#- source
%doc %{_texmfdistdir}/source/latex/frontespizio/frontespizio.dtx
%doc %{_texmfdistdir}/source/latex/frontespizio/frontespizio.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
