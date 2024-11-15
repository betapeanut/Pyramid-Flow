from huggingface_hub import snapshot_download

snapshot_download("rain1011/pyramid-flow-miniflux", local_dir="pyramid_flow_model", repo_type='model')
