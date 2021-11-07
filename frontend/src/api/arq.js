import request from '@/utils/request'

//  index
export function index(query) {
  return request({
    url: `/arq/index`,
    method: 'GET',
    params: query
  })
}

//  get_all_workers
export function get_all_workers(query) {
  return request({
    url: `/arq/get_all_workers`,
    method: 'GET',
    params: query
  })
}

//  get_task_list
export function get_task_list(query) {
  return request({
    url: `/arq/get_all_task`,
    method: 'GET',
    params: query
  })
}

//  get_all_result
export function get_all_result(query) {
  return request({
    url: `/arq/get_all_result`,
    method: 'GET',
    params: query
  })
}



