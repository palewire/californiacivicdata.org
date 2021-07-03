.PHONY: serve upload build

serve:
	bundle exec jekyll serve --watch

build:
	bundle exec jekyll build

upload:
	aws s3 cp ./_site s3://www.californiacivicdata.org/ --recursive --acl=public-read
