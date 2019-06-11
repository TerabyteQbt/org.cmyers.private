# Downloaded From...

* [multiaudience](https://ctan.org/tex-archive/macros/latex/contrib/multiaudience) - http://mirrors.ctan.org/macros/latex/contrib/multiaudience.zip
* [environ](https://ctan.org/pkg/environ) - http://mirrors.ctan.org/macros/latex/contrib/environ.zip
* [trimspaces](https://ctan.org/pkg/trimspaces) - http://mirrors.ctan.org/macros/latex/contrib/trimspaces.zip

environ and trimspaces are a dep of multiaudience

To generate the STY file, download, extract, find the .ins file, and run it through latex.

    $ latex multiaudience.ins && git add multiaudience.sty
    $ latex environ.ins && git add environ.sty
