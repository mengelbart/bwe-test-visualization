# Bandwidth Estimatin Visualizations

## Log format

The script expects a directory with the following contents:

```
.
├── receive_log
│   ├── rtcp_out.log
│   └── rtp_in.log
└── send_log
    ├── cc.log
    ├── rtcp_in.log
    └── rtp_out.log
```

### RTP Log (`rtp_in.log`/`rtp_out.log`)

```
<send-/receive-timestamp>, <payload-type>, <ssrc>, <sequence-number>, <rtp-timestamp>, <marker>, <size>, [<custom-field>, ...]
```

| Field | Content |
|-------|---------|
| `<send-/receive-timestamp>` | `int` Unix timestamp of the time when a packet was sent/received in ms since epoch. |
| `<payload-type>` | `int` RTP payload type |
| `<ssrc>` | `int` SSRC to which the packet belongs |
| `<sequence-number>` | `int` Sequence number of the RTP packet |
| `<rtp-timestamp>` | `int` RTP timestamp of the RTP packet |
| `<marker>` | `0|1` Value of the marker bit |
| `<size>` | `int` Size of the RTP packet when marshalled |

The RTP log format is taken from [RFC
8868](https://www.rfc-editor.org/rfc/rfc8868.html#name-rtp-log-format).

### Congestion Controller log

```
<timestamp>, <target-bitrate>
```

| Field | Content |
|-------|---------|
| `<timestamp>` | `int` Unix timestamp of the estimation |
| `<target-bitrate>` | `int` New target bitrate in bit/s |


