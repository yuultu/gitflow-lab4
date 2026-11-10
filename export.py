import csv


def export_csv(items, stream):
    """Write one item per row to a CSV text stream."""
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["item"])
    writer.writerows([item] for item in items)
