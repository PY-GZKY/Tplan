import request from '@/utils/request'

// 节点列表
export const host_list = query => {
    return request({
        url: `/hosts`,
        method: 'GET',
        params:query
    })
};


// 节点详情
export const host_detail  = query => {
    return request({
        url: `/host/detail`,
        method: 'GET',
        params:query
    })
};

// 创建节点
export const create_host  = data => {
    return request({
        url: `/host/create`,
        method: 'POST',
        data:data
    })
};

// 编辑节点信息
export const update_host  = data => {
    return request({
        url: `/host/update`,
        method: 'PUT',
        data: data
    })
};

// 删除节点
export const delete_host  = data => {
    return request({
        url: `/host/delete`,
        method: 'DELETE',
        data: data
    })
};


// 测试节点
export const test_host  = data => {
    return request({
        url: `/host/test`,
        method: 'POST',
        data: data
    })
};

// 节点部署服务
export const deploy_server  = data => {
    return request({
        url: `/host/deploys`,
        method: 'PUT',
        data: data
    })
};