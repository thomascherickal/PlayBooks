import React from "react";
import { currentWorkflowSelector } from "../../../../store/features/workflow/workflowSlice.ts";
import { useSelector } from "react-redux";
import SlackTriggerForm from "../../triggers/SlackTriggerForm";
import CopyCode from "../../../common/CopyCode/index.jsx";

function HandleWorkflowType() {
  const currentWorkflow = useSelector(currentWorkflowSelector);

  switch (currentWorkflow.workflowType) {
    case "slack":
      return <SlackTriggerForm />;

    case "api-trigger":
      if (currentWorkflow.curl)
        return (
          <div className="flex flex-col gap-2 lg:w-1/2">
            <CopyCode content={currentWorkflow.curl} language={"curl"} />
            <p className="text-sm p-2 border border-violet-500 bg-violet-50 rounded">
              Convert this curl into any language of your choice using{" "}
              <a
                className="underline text-violet-500"
                href="https://curlconverter.com/"
                target="_blank"
                rel="noreferrer">
                https://curlconverter.com/
              </a>
              .
            </p>
          </div>
        );
      else return <></>;

    default:
      return <></>;
  }
}

export default HandleWorkflowType;
