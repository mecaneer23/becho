count_down_from() {
	alacritty -o font.size=30 -o window.title="Count Down From $2" -e "$1"count_down_from_ $2
}

count_down_from $1 $#