#!/usr/bin/env python
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from matplotlib.ticker import EngFormatter
from jinja2 import Environment, FileSystemLoader

def plot_rates():
    cc_df = pd.read_csv(
        'testdata/send_log/cc.log',
        index_col = 0,
        names = ['time', 'target bitrate'],
        header = None,
        usecols = [0, 1],
    )
    cc_df.index = pd.to_datetime(cc_df.index - cc_df.index[0], unit='ms')

    rtp_out_df = pd.read_csv(
        'testdata/send_log/rtp_out.log',
        index_col = 0,
        names = ['time', 'RTP bit/s sent'],
        header = None,
        usecols = [0, 6],
    )
    rtp_out_df.index = pd.to_datetime(rtp_out_df.index - rtp_out_df.index[0], unit='ms')
    rtp_out_df['RTP bit/s sent'] = rtp_out_df['RTP bit/s sent'].apply(lambda x: x * 8)
    rtp_out_df = rtp_out_df.resample('1s').sum()

    rtp_in_df = pd.read_csv(
        'testdata/receive_log/rtp_in.log',
        index_col = 0,
        names = ['time', 'RTP bit/s received'],
        header = None,
        usecols = [0, 6],
    )
    rtp_in_df.index = pd.to_datetime(rtp_in_df.index - rtp_in_df.index[0], unit='ms')
    rtp_in_df['RTP bit/s received'] = rtp_in_df['RTP bit/s received'].apply(lambda x: x * 8)
    rtp_in_df = rtp_in_df.resample('1s').sum()


    fig, ax = plt.subplots(figsize=(8,2), dpi=400)

    l1, = ax.plot(cc_df.index, cc_df.values, label='Target Bitrate')
    l2, = ax.plot(rtp_out_df.index, rtp_out_df.values, label='RTP sent')
    l3, = ax.plot(rtp_in_df.index, rtp_in_df.values, label='RTP received')

    plt.xlabel('time')
    plt.ylabel('rate')
    ax.legend(handles=[l1, l2, l3])
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%M:%S"))
    ax.yaxis.set_major_formatter(EngFormatter(unit='bit/s'))
    
    plt.savefig('testdata/plot.png')

def generate_html():
    templates_dir = 'templates/'
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('detail.html')


    filename = os.path.join('testdata/', 'detail.html')
    with open(filename, 'w') as fh:
        fh.write(template.render())

def main():
    plot_rates()
    generate_html()

if __name__ == "__main__":
    main()

