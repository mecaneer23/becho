count_down_from() {
	alacritty -o font.size=30 -o window.title="Count Down From $1" -e /path/to/count_down_from_ $1
}

count_down_from $1