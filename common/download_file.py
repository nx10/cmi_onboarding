import pathlib as pl
from os import PathLike


def download_file(file_destination: str | PathLike, url_source: str, overwrite=False) -> pl.Path:
    """
    Download file from URL.

    :param file_destination:  Destination filepath.
    :param url_source: Source URL.
    :param overwrite: Overwrite if file exists.
    :return: Destination path (for chaining).
    """
    file_destination = pl.Path(file_destination)
    if overwrite or not file_destination.exists():
        import urllib.request
        _ = urllib.request.urlretrieve(url_source, file_destination)
    return file_destination
