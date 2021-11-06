import request from '@/utils/request'


//  nodes supervisor 获取所有 node
export function get_nodes() {
    return request({
        url: `/supervisor/nodes`,
        method: 'GET',
    })
}

//  node
export function get_node(node_name) {
    return request({
        url: `/supervisor/nodes/${node_name}`,
        method: 'GET',
        // params: query
    })
}

//  node 下的所有 processes
export function get_node_processes(node_name, query) {
    return request({
        url: `/supervisor/nodes/${node_name}/processes`,
        method: 'GET',
        params: query
    })
}




//  node  下的唯一 unique_process
export function get_process(node_name, unique_process_name, query) {
    return request({
        url: `/supervisor/nodes/${node_name}/process/${unique_process_name}`,
        method: 'GET',
        params: query
    })
}


// 开启  node  下的唯一 unique_process
export function start_process(node_name, unique_process_name, data) {
    return request({
        url: `/supervisor/nodes/${node_name}/process/${unique_process_name}/start`,
        method: 'PUT',
        data
    })
}



// 停止  node  下的唯一 unique_process
export function stop_process(node_name, unique_process_name) {
    return request({
        url: `/supervisor/nodes/${node_name}/process/${unique_process_name}/stop`,
        method: 'PUT',
    })
}


// 重启  node  下的唯一 unique_process
export function restart_process(node_name, unique_process_name) {
    return request({
        url: `/supervisor/nodes/${node_name}/process/${unique_process_name}/restart`,
        method: 'PUT',
    })
}


// node  下的唯一 unique_process  日志
export function read_process_log(node_name, unique_process_name) {
    return request({
        url: `/supervisor/nodes/${node_name}/process/${unique_process_name}/log`,
        method: 'GET',
    })
}



// 重启  node  下的所有 process
export function start_all_process(node_name, data) {
    return request({
        url: `/supervisor/nodes/${node_name}/all-processes/start`,
        method: 'PUT',
        data
    })
}



// 停止  node  下的所有 process
export function stop_all_process(node_name, data) {
    return request({
        url: `/supervisor/nodes/${node_name}/all-processes/stop`,
        method: 'PUT',
        data
    })
}


// 重启  node  下的所有 process
export function restart_all_process(node_name, data) {
    return request({
        url: `/supervisor/nodes/${node_name}/all-processes/restart`,
        method: 'PUT',
        data
    })
}