/* eslint-disable react-hooks/exhaustive-deps */
import { useNavigate } from "react-router-dom";
import Heading from "../Heading";
import { useEffect, useState } from "react";
import SuspenseLoader from "../Skeleton/SuspenseLoader";
import TableSkeleton from "../Skeleton/TableLoader";
import { useGetWorkflowsQuery } from "../../store/features/workflow/api/getWorkflowsApi.ts";
import WorkflowTable from "./WorkflowTable.jsx";

const Workflows = () => {
  const navigate = useNavigate();
  const [pageMeta, setPageMeta] = useState({ limit: 10, offset: 0 });
  const { data, isFetching, refetch } = useGetWorkflowsQuery(pageMeta);
  const workflowsList = data?.workflows;
  const total = data?.meta?.total_count;

  useEffect(() => {
    if (!isFetching) refetch(pageMeta);
  }, [pageMeta]);

  const pageUpdateCb = (page) => {
    setPageMeta(page);
  };

  const handleCreateWorkflow = () => {
    navigate({
      pathname: "/workflows/create",
    });
  };

  return (
    <div>
      <Heading
        heading={"Workflows"}
        onTimeRangeChangeCb={false}
        onRefreshCb={false}
      />
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          padding: "1.5rem",
          justifyContent: "space-between",
        }}>
        <button
          className="text-sm bg-violet-600 hover:bg-violet-700 px-4 py-2 rounded-lg create_playbook"
          onClick={handleCreateWorkflow}
          style={{ color: "white", marginTop: "0px", marginRight: "10px" }}>
          + Create Workflow
        </button>
      </div>
      <SuspenseLoader loading={isFetching} loader={<TableSkeleton />}>
        <WorkflowTable
          workflowsList={workflowsList}
          total={total}
          pageSize={pageMeta ? pageMeta?.limit : 10}
          pageUpdateCb={pageUpdateCb}
          tableContainerStyles={
            workflowsList?.length
              ? {}
              : { maxHeight: "35vh", minHeight: "35vh" }
          }
          refreshTable={refetch}></WorkflowTable>
      </SuspenseLoader>
    </div>
  );
};

export default Workflows;
