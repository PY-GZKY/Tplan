import request from '@/utils/request'

export function get_data_list(query) {
  return request({
    url: '/xhs/list',
    method: 'get',
    params: query
  })
}


export function get_xhs_list(query) {
  return request({
    url: '/xhs/list',
    method: 'get',
    params: query
  })
}

