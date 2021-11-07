<template>
  <div class="app-container">
    <el-row :gutter="20">
      <el-col :span="20" :xs="24">
        <el-form
          ref="listQuery"
          :model="listQuery"
          :inline="true"
          label-width="68px"
        >
          <el-form-item label="">
            <el-select
              v-model="listQuery.worker"
              placeholder="工人"
              clearable
              style="width: 130px"
              size="mini"
              @change="handleFilter"
            >
              <el-option label="所有" key="" value="" />
              <el-option
                v-for="item in workerList"
                :key="item.worker_name"
                :label="item.worker_name"
                :value="item.worker_name"
              />
            </el-select>
          </el-form-item>

          <el-form-item label="">
            <el-select
              v-model="listQuery.task"
              placeholder="任务"
              clearable
              style="width: 130px"
              size="mini"
              @change="handleFilter"
            >
              <el-option label="所有" key="" value="" />
              <el-option
                v-for="item in taskList"
                :key="item.function_ms"
                :label="item.function_name"
                :value="item.function_name"
              />
            </el-select>
          </el-form-item>

          <el-form-item label="">
            <el-select
              v-model="listQuery.status"
              placeholder="状态"
              clearable
              style="width: 130px"
              size="mini"
              @change="handleFilter"
            >
              <el-option label="所有" key="" value="" />
              <el-option
                v-for="item in statusList"
                :key="item.us"
                :label="item.zh"
                :value="item.us"
              />
            </el-select>
          </el-form-item>

          <el-form-item>
            <el-input
              placeholder="任务ID"
              clearable
              size="mini"
              style="width: 200px"
              @keyup.enter.native="handleFilter"
            />
          </el-form-item>
          <el-form-item label="">
            <el-date-picker
              v-model="listQuery.start_time"
              type="datetimerange"
              size="mini"
              align="right"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              :default-time="['12:00:00', '08:00:00']"
            >
            </el-date-picker>
          </el-form-item>
          <el-form-item>
            <el-button
              v-waves
              type="primary"
              size="mini"
              icon="el-icon-search"
              @click="handleFilter"
            >
              搜索
            </el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>

    <el-table
      :key="tableKey"
      :data="taskList_"
      aria-setsize
      fit
      highlight-current-row
      style="width: 100%"
    >
      <el-table-column min-width="290px" align="center" label="任务ID">
        <template slot-scope="{ row }">
          <el-button type="text" @click="jobResult(row)">{{
            row.job_id
          }}</el-button>
        </template>
      </el-table-column>

      <el-table-column min-width="340px" align="center" label="工作者">
        <template slot-scope="{ row }">
          <el-button type="" plain>{{ row.worker_name }}</el-button>
        </template>
      </el-table-column>

      <el-table-column min-width="120px" align="center" label="任务名称">
        <template slot-scope="{ row }">
          <el-button type="primary" plain>{{ row.function }}</el-button>
        </template>
      </el-table-column>

      <el-table-column min-width="120px" align="center" label="任务参数">
        <template slot-scope="{ row }">
          <span>{{ row.args || "-" }}</span>
        </template>
      </el-table-column>
      <el-table-column min-width="150px" align="center" label="字典参数">
        <template slot-scope="{ row }">
          <span>{{ row.kwargs || "-" }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="120px" align="center" label="重试次数">
        <template slot-scope="{ row }">
          <span>{{ row.job_try || "-" }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="140px" align="center" label="状态">
        <template slot-scope="{ row }">
          <el-button
            v-if="row.state == 'complete'"
            type="success"
            size="mini"
            plain
            ><i class="el-icon-success"></i>完成</el-button
          >
          <el-button
            v-else-if="row.state == 'queued'"
            type="warning"
            size="mini"
            plain
            ><i class="el-icon-more"></i>等待</el-button
          >
          <el-button
            v-else-if="row.state == 'in_progress'"
            type="warning"
            :loading="true"
            size="mini"
            plain
            >进行中</el-button
          >
          <el-button
            v-else-if="row.state == 'failed'"
            type="error"
            size="mini"
            plain
            ><i class="el-icon-error"></i>失败</el-button
          >
          <el-button v-else type="" size="mini" plain>{{
            row.state
          }}</el-button>
        </template>
      </el-table-column>

      <el-table-column min-width="270px" align="center" label="开始时间">
        <template slot-scope="{ row }">
          <el-button type="" size="mini" plain>{{
            row.start_time || row.enqueue_time
          }}</el-button>
        </template>
      </el-table-column>

      <el-table-column min-width="270px" align="center" label="结束时间">
        <template slot-scope="{ row }">
          <el-button type="" size="mini" plain>{{
            row.finish_time || "待定"
          }}</el-button>
        </template>
      </el-table-column>

      <el-table-column min-width="200px" align="center" label="运行时长">
        <template slot-scope="{ row }">
          {{ row.expire_time || "待定" }}
        </template>
      </el-table-column>

      <el-table-column min-width="140px" align="center" label="成功">
        <template slot-scope="{ row }">
          <el-button
            v-if="row.success == true"
            type="success"
            icon="el-icon-check"
            circle
          ></el-button>
          <el-button
            v-else-if="row.success == false"
            type="danger"
            icon="el-icon-delete"
            circle
          ></el-button>
          <el-button v-else type="text" size="mini" plain>待定</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination
      v-show="total > 0"
      :total="total"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.limit"
      @pagination="getList"
    />
  </div>
</template>

<script>
import { get_all_result, get_all_workers, get_task_list } from "@/api/arq";
import waves from "@/directive/waves"; // waves directive
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

export default {
  inject: ["reload"],
  name: "jobList",
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      taskList_: null,
      taskList: null,
      workerList: null,
      statusList: [
        { us: "complete", zh: "完成" },
        { us: "failed", zh: "失败" },
        { us: "in_progress", zh: "进行中" },
        { us: "queued", zh: "等待中" },
      ],
      total: 0,
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 10,
        worker: null,
        task: null,
        status: null,
        job_id_: null,
        start_time: null,
        end_time: null
      },
    };
  },
  created() {
    this.getList();
    this.getWorkerKeys();
    this.getTaskKeys();
  },
  methods: {
    getList() {
      get_all_result(this.listQuery).then((response) => {
        this.taskList_ = response.results;
        this.total = response.total || 2;
        setTimeout(() => {}, 1.5 * 1000);
      });
    },

    getWorkerKeys() {
      get_all_workers({}).then((response) => {
        this.workerList = response.result;
        setTimeout(() => {}, 1.5 * 1000);
      });
    },

    getTaskKeys() {
      get_task_list({}).then((response) => {
        this.taskList = response.results.task_list;
        this.taskList = this.taskList.concat(response.results.cron_list);
        setTimeout(() => {}, 1.5 * 1000);
      });
    },

    handleFilter() {
      this.listQuery.page = 1;
      this.getList();
    },

    deleteTask(taskId) {
      const self = this;
      var data = {
        taskId,
      };
      // 二次确认删除
      self
        .$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          delete_task(data).then((res) => {
            if (res.code === 20000) {
              self.$message.success("删除成功");
              self.reload();
            }
          });
        })
        .catch(() => {});
    },

    jobResult(row) {
      this.$router.push(`/result/${row.job_id}`);
    },
  },
};
</script>
