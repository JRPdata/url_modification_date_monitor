# url_file_modification_date_monitor
Monitor urls (http/ftp) for changes by polling the modification date from a HEAD request and notify when they change.

Must have protocol in conf (http:// or ftp://).

If a ftp url requires a username/pass other than anonymous/anonymous, specify it as ftp://username:password@server.com/path/to/file

Based on code from url_file_size_monitor_monitor (and url_file_size_monitor) for github.

See https://github.com/JRPdata/commit_file_monitor for general setup notes.

The notable difference is the confs for each url in conf/url only have one line (the url).
