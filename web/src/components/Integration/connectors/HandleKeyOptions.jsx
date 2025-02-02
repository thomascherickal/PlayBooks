import React from "react";
import ValueComponent from "../../ValueComponent";
import { useDispatch, useSelector } from "react-redux";
import {
  connectorSelector,
  setKey,
} from "../../../store/features/integrations/integrationsSlice.ts";
import Checkbox from "../../common/Checkbox/index.tsx";

function HandleKeyOptions({ option, connectorActive, value, onValueChange }) {
  const dispatch = useDispatch();
  const currentConnector = useSelector(connectorSelector);

  switch (option.display_name) {
    case "PEM":
      return (
        <textarea
          disabled={connectorActive}
          value={value ?? currentConnector[option.key_type]}
          placeHolder={`Enter ${option.display_name}`}
          onChange={(e) => {
            if (onValueChange) {
              onValueChange(e.target.value);
              return;
            }
            dispatch(setKey({ key: option.key_type, value: e.target.value }));
          }}
          className="border rounded-lg h-40 lg:max-w-1/2 max-w-full mr-2 p-2 w-[500px] resize-none text-xs outline-none"
        />
      );
    case "Enable TLS certificate validation":
      return (
        <Checkbox
          id="ssl-verify"
          disabled={connectorActive}
          isChecked={
            value
              ? value === "true"
              : currentConnector[option.key_type]?.toString() === "true"
          }
          onChange={() => {
            const currVal = currentConnector[option.key_type];
            if (onValueChange) {
              onValueChange(
                value === "false" || value === "" ? "true" : "false",
              );
              return;
            }
            dispatch(setKey({ key: option.key_type, value: !currVal }));
          }}
        />
      );
    default:
      return (
        <ValueComponent
          valueType={"STRING"}
          onValueChange={(val) => {
            if (onValueChange) {
              onValueChange(val);
              return;
            }
            dispatch(setKey({ key: option.key_type, value: val }));
          }}
          disabled={connectorActive}
          value={value ?? currentConnector[option.key_type]}
          placeHolder={option.display_name}
          length={500}
        />
      );
  }
}

export default HandleKeyOptions;
